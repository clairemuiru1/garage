import React, { useState, useEffect } from "react";

function UpdateSparePart({ sparePartId }) {
  const [sparePart, setSparePart] = useState({
    name: "",
    description: "",
    price: 0,
    image: "",
  });

  useEffect(() => {
    // Fetch the spare part details using sparePartId when the component mounts
    fetch(`http://127.0.0.1:5555/sparepart/${sparePartId}`)
      .then((response) => response.json())
      .then((data) => setSparePart(data))
      .catch((error) => console.error("Error fetching spare part:", error));
  }, [sparePartId]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSparePart((prevSparePart) => ({
      ...prevSparePart,
      [name]: value,
    }));
  };

  const handleUpdate = (e) => {
    e.preventDefault();

    // Check if sparePartId is defined
    if (sparePartId) {
      // Send a PATCH request to update the spare part
      const apiUrl = `http://127.0.0.1:5555/sparepart/${sparePartId}`;
      fetch(apiUrl, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(sparePart),
      })
        .then((response) => {
          console.log("Response status:", response.status);
          return response.json();
        })
        .then((data) => {
          console.log("Spare part updated successfully:", data);
          // Optionally, you can redirect the user or perform other actions
        })
        .catch((error) => console.error("Error updating spare part:", error));
    } else {
      // console.error("Error: sparePartId is undefined");
    }
  };

  return (
    <div>
      <h2>Update Spare Part</h2>
      <form onSubmit={handleUpdate}>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={sparePart.name}
          onChange={handleInputChange}
        />

        <label htmlFor="description">Description:</label>
        <input
          type="text"
          id="description"
          name="description"
          value={sparePart.description}
          onChange={handleInputChange}
        />

        <label htmlFor="price">Price:</label>
        <input
          type="number"
          id="price"
          name="price"
          value={sparePart.price}
          onChange={handleInputChange}
        />

        <label htmlFor="image">Image URL:</label>
        <input
          type="text"
          id="image"
          name="image"
          value={sparePart.image}
          onChange={handleInputChange}
        />

        <button type="submit">Update Spare Part</button>
      </form>
    </div>
  );
}

export default UpdateSparePart;
