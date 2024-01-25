import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './Login';
import Service from './Service';
import Signup from './Signup';
import Home from './Home';
import Garage from './Garage';
import Sparepart from './Sparepart';
import Navbar from './Navbar';

import '../index.css';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/garage/:id" element={<Garage />} />
            <Route path="/service" element={<Service />} />
            <Route path="/sparepart" element={<Sparepart />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;