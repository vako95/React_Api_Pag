import MoovieShow from "./services/movie-show";
import MoovieDetail from "./components/MoovieDetail/MoovieDetail";
import MovieList from "./components/MoovieList/MovieList";

import { useEffect, useState } from "react";
import { BACKDROP_IMG } from "./config";

import Logo from "./components/Logo/Logo";
import LogoImg from './assets/img/logo.svg'
import { Container, Row } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';
import s from './style.module.css'





function App() {
  const [currentMoovie, setCurrentMoovie] = useState({});
  const [tvShowRecomendations,setTvShowRecomendations] = useState([])
  const [tvVideos,setTvVideos] = useState([])

async function fetVideo(id){
  const responser = await MoovieShow.fetVideo(id);
  setTvVideos(responser)
  // console.log(respons)
  
}

  async function fetchData() {
    try {
      const responser = await MoovieShow.fetchMoovie()
      setCurrentMoovie(responser)
    } catch (err) {
      console.log(err)
    }
  }

  async function fetchRecomendations(id) {
    try{
      const responser = await MoovieShow.fetchRecomendations(id)
      setTvShowRecomendations(responser.data.results.splice(0,6))
      
    }catch(err){
         console.log(err)
    }
  }


  useEffect(() => {
    fetchData()
    return () => {
      setCurrentMoovie({})
    }
  }, [])


  function updatecurrentMoovie(tvShow){
    setCurrentMoovie(tvShow);
  }
// console.log(currentMoovie.id)
//   useEffect(() => {
//     fetchRecomendations(currentMoovie.id)
//     return() => {
//      setTvShowRecomendations([])
//     }
//   },[currentMoovie.id])
  // console.log(tvShowRecomendations)
  useEffect(() => {
    
    if (currentMoovie.id) {
      fetchRecomendations(currentMoovie.id);
    }
    return() => {
           setTvShowRecomendations([])
          }
  }, [currentMoovie.id]);
  
  useEffect(() => {
    if(currentMoovie.id){
      fetVideo(currentMoovie.id);
    }
   return () => {
   setTvVideos([])

   }
  },[currentMoovie.id])


  return (
  <Container fluid className="mb-1">
      <Row>
        <Logo img={LogoImg} />

        <div className={s.imgr} style={{
          overflow: 'hidden',
          background: currentMoovie
            ? `linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55)),
               url("${BACKDROP_IMG}${currentMoovie.backdrop_path}") no-repeat center / cover `
            : 'blue',
         
        }}>
          {currentMoovie && <MoovieDetail tvShow={currentMoovie} />}
          {currentMoovie && <MovieList
          tvVideo={tvVideos} 
          tvShowList={tvShowRecomendations}
          onClikcItem={updatecurrentMoovie}
          />}
        </div>


      </Row>

    </Container>



  )
}

export default App;