// App.js

import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './Login';
import Service from './Service';
import Signup from './Signup';
import Home from './Home';
import Garage from './Garage';
import Sparepart from './Sparepart';
import Navbar from './Navbar';
import UpdateSparePart from './UpdateSparepart'; // Corrected import statement
import '../index.css';

function App() {
  const [loggedInUser, setLoggedInUser] = useState(null);

  const handleLogin = (user) => {
    console.log("Logged in user:", user);
    setLoggedInUser(user);
  };

  return (
    <Router>
      <div>
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home loggedInUser={loggedInUser} />} />
            <Route path="/garage/:id" element={<Garage />} />
            <Route path="/service" element={<Service />} />
            <Route path="/sparepart" element={<Sparepart />} />
            <Route path="/login" element={<Login onLogin={handleLogin} />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="*" element={<Navigate to="/" />} />
            <Route path="/update-spare-part/:id" element={<UpdateSparePart />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
