import React, { useEffect, useState } from "react";

function Service() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/service")
      .then((response) => response.json())
      .then(setServices);
  }, []); // No need to include setServices in the dependency array

  const handleTowButtonClick = () => {
    alert("Tow truck will arrive in 1 hour");
  };

  const handleMechanicButtonClick = () => {
    alert("Mechanic arrives in 30 mins");
  };

  return (
    <section>
      <h2>Services</h2>
      <ul>
        {services.map((serviceItem) => (
          <li key={serviceItem.id}>
            <p>Name: {serviceItem.name}</p>
            <p>Description: {serviceItem.description}</p>
            <p>Price: {serviceItem.price}</p>
            <button onClick={handleTowButtonClick}>Tow a Car</button>
            <button onClick={handleMechanicButtonClick}>Dial a Mechanic</button>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Service;