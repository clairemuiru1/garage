// App.js

import React, { useEffect, useState } from 'react';

const App = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSignup = (event) => {
    event.preventDefault();

    // Use setUsername, setEmail, and setPassword functions as needed
    setUsername('newUsername');
    setEmail('newEmail');
    setPassword('newPassword');

    // Make a POST request to signup endpoint
    fetch('http://127.0.0.1:5555/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username,
        email: email,
        password: password,
      }),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
        // Handle the response as needed
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const handleLogin = (event) => {
    event.preventDefault();

    // Use setUsername, setEmail, and setPassword functions as needed
    setUsername('newUsername');
    setEmail('newEmail');
    setPassword('newPassword');

    // Make a POST request to login endpoint
    fetch('http://127.0.0.1:5555/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
        // Handle the response as needed
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  useEffect(() => {
    // Fetch and display the list of garages
    fetch('http://127.0.0.1:5555/garage')
      .then(response => response.json())
      .then(data => {
        // Assuming data is an array of garages
        data.forEach(garage => {
          // Process each garage
        });
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []); // Empty dependency array to ensure useEffect runs once on mount

  return (
    <div>
      <form onSubmit={handleSignup}>
        {/* Your signup form fields */}
        <button type="submit">Sign Up</button>
      </form>

      <form onSubmit={handleLogin}>
        {/* Your login form fields */}
        <button type="submit">Login</button>
      </form>

      {/* Your React components and UI elements */}
    </div>
  );
};

export default App;




   