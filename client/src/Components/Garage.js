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
      <h2>Garage Details</h2>
      <p>Name: {garage.name}</p>
      <p>Location: {garage.location}</p>

      <h3>Services</h3>
      {garage.Service && garage.Service.length > 0 ? (
        <ul>
          {garage.Service.map((service) => (
            <li key={service.id}>{service.name}</li>
          ))}
        </ul>
      ) : (
        <p>No services available for this garage.</p>
      )}
    </div>
  );
}

export default Garage;
