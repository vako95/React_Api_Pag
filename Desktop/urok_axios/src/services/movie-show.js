import axios from 'axios'
import { BASE_URL,API_KEY } from '../config'




class MoovieShow  {
 static async fetchMoovie() {
    const response = await axios.get(`${BASE_URL}movie/popular${API_KEY}`)
    return response.data.results[0]
   
 }

 static async fetchRecomendations (series_id) {
  
   const response = await axios.get(`${BASE_URL}movie/${series_id}/recommendations${API_KEY}`)
   return response ;
   
 }
 static async fetVideo(series_id){
  const response = await axios.get(`${BASE_URL}movie/${series_id}/videos${API_KEY}`)
  return response.data.results
  // console.log(response.data.results)
 }


}

export default MoovieShow;
