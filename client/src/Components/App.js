import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Added missing semicolon
// import Login from './Login';
// import Service from './Service';
// import Sparepart from './Sparepart';
// import Signup from './Signup'; // Corrected the component name
import Home from './Home';
// import Garage from './Garage';
import '../index.css';

function App() {
  return (
    <Router>
      <div>
        {/* <Header></Header>*/}
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            {/* <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/service" element={<Service />} />
            <Route path="/sparepart" element={<Sparepart />} />
            <Route path="/garage/:id" element={<Garage />} /> */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;




   