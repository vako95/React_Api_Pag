
import React, {useState, useEffect} from 'react'
import { createClient } from 'pexels';
import './InfoApp.css'


const InfoApp = () => {
  const[loading,setLoading] = useState(true)
  const[photor,setPhotor] = useState(null);
  const[page,setPage] = useState(1)

  const client = createClient('JEVr30L44x1pr7n5beH7sYyl8Wf1tdV7pKVnOIo1ONfD8zeqXUkDRdAM');
  useEffect(() => {
    setLoading(true);
      client.photos.curated({per_page:30, page: page }).then((res) => {
console.log(res)
     setPhotor(res.photos)

  }).catch((err)=>console.log(err)).finally(()=>setLoading(false))

  },[page])



  const nextPage = () => {
    setPage(page + 1);
  };

  const prevPage = () => {
    if (page > 1) {
      setPage(page - 1)
    }
  };

  return(
    <div className="info">
      {loading?(
        <div className='white-text'>Loading...</div>
      ):(
        <>
        <p>Image Gallery</p>
        {photor&&photor.length>0?(
          <div className='img_con'>
            {photor.map((data) => (
              <div className='imager' key={data.id}>
                <img src={data.src.landscape} alt={data.alt} />
              </div>
            ))}
          </div>
        ):(
          <div className='white-text'>No Photos Found</div>
        )}
        <div>
          <button onClick={prevPage} disabled={page === 1}>Prev</button>
          <button onClick={nextPage}>Next</button>
        </div>
        </>
      )}
    </div>
  )
}


export default InfoApp;