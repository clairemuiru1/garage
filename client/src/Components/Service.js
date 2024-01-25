import { useEffect, useState } from "react";

function Service() {
  const [service, setService] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/service")
      .then((response) => response.json())
      .then(setService);
  }, [setService]); // Add setService to the dependency array

  return (
    <section>
      <h2>Service</h2>
      <ul>
        {service.map((serviceItem) => (
          <li key={serviceItem.id}>
            <a href={`${window.location.origin}/service/${serviceItem.id}`}>
              {serviceItem.name}
            </a>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Service;


