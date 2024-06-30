import React from 'react'
import {Route, Routes} from 'react-router-dom'


import Layout from '../Layout/Layout';
import Home from '../Home/Home'
import About from '../About/About'
import Contact from '../Contact/Contact'
import PageNotFound from '../NotFound/PageNotFound'




const App = () => {

    return(
    <Routes>
        <Route path='/' element={<Layout/>}>
        <Route index element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/contact' element={<Contact/>}/>
        <Route path='*' element={<PageNotFound/>}/>
    
        </Route>
    </Routes>
    )
}


export default App;