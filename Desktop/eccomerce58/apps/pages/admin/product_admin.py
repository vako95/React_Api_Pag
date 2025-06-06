from django.contrib import admin
from ..models import Product
from ..models import ProductTrash
from django.utils.timezone import now
from django.utils.safestring import mark_safe



class ProductAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        return qs.filter(time_deleted__isnull=True)
    
    actions = ("soft_delete", "hard_delete")
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        actions["hard_delete"] = (self.hard_delete, "hard_delete", "Hard Delete Selected")
        actions["soft_delete"] = (self.soft_delete, "soft_delete", "Soft Delete Selected")
        del actions["delete_selected"]
        return actions
    

    
 
    @admin.action(description="Soft delete selected items")
    def soft_delete(modeladmin,self, request, queryset):
        for obj in queryset:
            obj.time_deleted = now()
            obj.save()

    @admin.action(description="Hard delete selected items")
    def hard_delete(self,modeladmin, request, queryset):
        queryset.delete()

    def changelist_view(self, request, extra_context=None):
        ProductTrash._meta.verbose_name_plural =f"Product Trash ({ProductTrash.objects.filter(time_deleted__isnull=False).count()})"
        return super().changelist_view(request, extra_context)     

admin.site.register(Product,ProductAdmin)



class ProductTrashAdmin(admin.ModelAdmin):
    view_on_site = False
    actions = ["restore", "hard_delete"]
    readonly_fields = ("time_deleted",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(time_deleted__isnull=False)

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions["restore"] = (self.restore, "restore", "Restore back to Products")
        del actions["delete_selected"]
        return actions

    @admin.action(description="Hard delete selected items")
    def hard_delete(modeladmin, request, queryset):
        queryset.delete()


    @admin.action(description="Restore")
    def restore(self,modeladmin, request, queryset):
        queryset.update(time_deleted=None)

    def changelist_view(self, request, extra_context=None):
        self.model._meta.verbose_name_plural =f"Product Trash ({self.model.objects.filter(time_deleted__isnull=False).count()})"
        return super().changelist_view(request, extra_context) 


    def has_add_permission(self, request):
        return False
    
    def get_model_perms(self, request):
        if ProductTrash.objects.filter(time_deleted__isnull=False).exists():
            return super().get_model_perms(request)
        return {}


admin.site.register(ProductTrash, ProductTrashAdmin)
    

  


