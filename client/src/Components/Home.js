import React, { useEffect, useState } from "react";

function Home() {
  const [garage, setGarage] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/garage")
      .then((response) => response.json())
      .then((data) => {
        setGarage(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setLoading(false);
      });
  }, [setGarage]);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <section>
      <h2>Garage Near You</h2>
      <ul>
        {garage.map((garageItem) => (
          <li key={garageItem.id}>
            <a href={`${window.location.origin}/garage/${garageItem.id}`}>
              {garageItem.name}
            </a>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Home;
