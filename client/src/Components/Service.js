import React, { useEffect, useState } from "react";

function Service() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/service")
      .then((response) => response.json())
      .then(setServices);
  }, []); // No need to include setServices in the dependency array

  return (
    <section>
      <h2>Services</h2>
      <ul>
        {services.map((serviceItem) => (
          <li key={serviceItem.id}>
         
            <p>Name: {serviceItem.name}</p>
            <p>Description: {serviceItem.description}</p>
            <p>Price: {serviceItem.price}</p>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Service;



