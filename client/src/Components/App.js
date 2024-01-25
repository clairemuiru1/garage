import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Added missing semicolon
import Login from './Login';
import Service from './Service';
import Signup from './Signup'; // Corrected the component name
import Home from './Home';
import Garage from './Garage';

import '../index.css';

function App() {
  return (
    <Router>
      <div>
        {/* <Header></Header>*/}
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/garage/:id" element={<Garage />} />
            <Route path="/service" element={<Service />} />
       
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            {/* 
            
            
        
             */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;




   