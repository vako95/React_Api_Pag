import {Row,Col} from 'react-bootstrap'
import s from './detail.module.css'
import FiveStarRaiting from '../FiveStarRating/FiveStarRaiting'
import strela from '../../assets/img/strela.png'



const MoovieDetail = ({tvShow}) => {


    return (
   
          <div className={s.detailContainer}>
                  <div className={s.content}>
                  <h2>{tvShow.title}</h2>
                  <FiveStarRaiting rating={tvShow.vote_average}  />
                  <div>{tvShow.vote_average / 2} / 5</div>
                  <div><p className={s.date}>Date: {tvShow.release_date}</p></div>
                  
                <div className="row">
                    <div className={`col-sm-12 col-lg-8 col-md-8 ${s.description}`}>
                    {
                    tvShow.overview
                  }
                    </div>
                </div>
                <div><h4>You'll probably like :<img className={s.strela} src={strela} alt="" /></h4></div>
                 
                    
    
            </div>
        </div>  
       
    )
}

export default MoovieDetail;