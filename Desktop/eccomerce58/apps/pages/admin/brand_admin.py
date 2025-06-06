from django.contrib import admin
from django.utils.html import format_html, mark_safe
from ..models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name_tag", "slug_with_link", "logo_tag", "time_create", "time_update", "status")
    list_display_links = ("name_tag",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("status", "time_create", "time_update")
    search_fields = ("name", "slug")
    readonly_fields = ("logo_tag", "time_create", "time_update")
    exclude = ("slug",)

    @admin.display(description="Name")
    def name_tag(self,obj):
        name_tag = obj.name if len(obj.name) <= 12 else obj.name + "..."
        return mark_safe(f"{name_tag}")
    
    @admin.display(description="Logo")
    def logo_tag(self, obj):
        if obj.logo:  
            return format_html(
                '''<a href="{0}" data-lity>
                <img src="{0}" style="width:100px; height:auto; border-radius:5px; object-fit:cover;"/>
                </a>''',
                obj.logo.url,
                obj.logo.url,
            )
        return "No Image"
        
    
    class Media:
        css = {"all": ("pages/lity/dist/lity.min.css",)}
        js = (
               "pages/lity/vendor/jquery.js",
               "pages/lity/dist/lity.min.js"
        )

    @admin.display(description="Slug")
    def slug_with_link(self,obj):
        slug_link_view = obj.slug if len(obj.slug) <= 12 else obj.slug + "..."
        slug_url = obj.get_absolute_url()
        return format_html(
            '<a src="{}" target="_blank">{} 🔗</a>',
            slug_url,
            slug_link_view,
        )

        
