import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Garage() {
  const { id } = useParams();
  const [garage, setGarage] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/garage/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => {
        setGarage(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setError(error);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>Error: {error.message}</h2>;
  }


  return (
    <div>
      <h1>{garage.name}</h1>
      <p>Contact Number: {garage.contact_number}</p>
      <p>Location: {garage.location}</p>

      {garage.services.map((service) => (
        <div key={service.id}>
          <h2>{service.name}</h2>
          <p>Description: {service.description}</p>
          <p>Price: ${service.price}</p>

          <h3>Spare Parts</h3>
          <ul>
            {service.spare_parts.map((part) => (
              <li key={part.id}>
                <h4>{part.name}</h4>
                <p>Description: {part.description}</p>
                <p>Price: ${part.price}</p>
                <img src={part.image} alt={part.name} style={{ maxWidth: "200px" }} />
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default Garage;

