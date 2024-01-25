import React, { useState, useEffect } from 'react';

const Sparepart = () => {
  const [spareParts, setSpareParts] = useState([]);

  useEffect(() => {
    const fetchSpareParts = async () => {
      try {
        const response = await fetch('http://localhost:5555/sparepart');
        const data = await response.json();
        setSpareParts(data);
      } catch (error) {
        console.error('Error fetching spare parts:', error);
      }
    };

    fetchSpareParts();
  }, []); 

  return (
    <div>
      <h2>Spare Parts List</h2>
      <ul>
        {spareParts.map((sparePart) => (
          <li key={sparePart.id}>
            <strong>{sparePart.name}</strong>
            <p>Description: {sparePart.description}</p>
            <p>Price: ${sparePart.price}</p>
            {sparePart.image && <img src={sparePart.image} alt={sparePart.name} />}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sparepart;