import { Outlet, NavLink,useLocation } from "react-router-dom";

import { Fragment } from "react";
import Footer from "../Footer/Footer";


import './Layout.css'
import InfoApp from "../content/InfoApp/InfoApp";
const myStyle = ({isActive}) => isActive ? 'myStyle nav' : 'nav'



const Layout = () => {
    const location = useLocation();
    return (
        <Fragment>
            <header>
        <NavLink className={myStyle} to='/'>Home</NavLink>
        <NavLink className={myStyle} to='/about'>About</NavLink>
        <NavLink className={myStyle} to='/contact'>Contact</NavLink>
            </header>
        <div className="lay">
            <Outlet/>
            {location.pathname === '/' && <InfoApp />}

        </div>
        
        <Footer />
        </Fragment>
    )
}

export default Layout;