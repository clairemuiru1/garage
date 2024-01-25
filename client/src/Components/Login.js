import React, { useState } from "react";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [userData, setUserData] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send username to the login endpoint
      const response = await fetch("http://127.0.0.1:5555/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username }),
      });

      if (!response.ok) {
        throw new Error("Failed to log in");
      }

      // If login is successful, fetch additional user data
      const user = await response.json();
      setUserData(user);

      // Trigger the onLogin callback
      onLogin(user);
    } catch (error) {
      console.error("Error logging in:", error);
      setError(error.message);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>

      {userData && (
        <div>
          <h2>Welcome, {userData.username}!</h2>
          <p>Email: {userData.email}</p>
          {/* Display other user data as needed */}
        </div>
      )}

      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default Login;

