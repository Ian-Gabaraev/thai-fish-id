import React, { useState } from "react";
import Select from "react-select";
import { Emojione } from "react-emoji-render";
import axios from "axios";

const SHAPE_OPTIONS = [
  { value: "rounded", label: <Emojione text="🔵 Rounded" size={16} /> },
  { value: "elongated", label: <Emojione text="🐠 Elongated" size={16} /> },
  { value: "flat", label: <Emojione text="🐟 Flat" size={16} /> },
];

const COLOR_OPTIONS = [
  { value: "red", label: "🔴 Red" },
  { value: "green", label: "🟢 Green" },
  { value: "blue", label: "🔵 Blue" },
  { value: "yellow", label: "🟡 Yellow" },
  { value: "pink", label: "💗 Pink" },
  { value: "white", label: "⚪ White" },
  { value: "black", label: "⚫ Black" },
  { value: "orange", label: " 🟠 Orange" },
];


const BEHAVIOR_OPTIONS = [
  { value: "aggressive", label: <Emojione text="👊 Aggressive" /> },
  { value: "non-aggressive", label: <Emojione text="😇 Peaceful" /> },
  { value: "semi-aggressive", label: <Emojione text="👿😇 Semi-aggressive" /> },
];

const FishFilter = () => {
  const [selectedShape, setSelectedShape] = useState("");
  const [selectedBehaviors, setSelectedBehaviors] = useState([]);
  const [selectedColors, setSelectedColors] = useState([]);
  const [selectedSize, setSelectedSize] = useState("");

  const handleShapeChange = (event) => {
    setSelectedShape(event.target.value);
  };

  const handleBehaviorChange = (selectedOptions) => {
    setSelectedBehaviors(selectedOptions.map((option) => option.value));
  };

  const handleColorChange = (selectedOptions) => {
    setSelectedColors(selectedOptions.map((option) => option.value));
  };

  const handleSizeChange = (event) => {
    setSelectedSize(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    let body = {};

    if (selectedShape) {
      body = { ...body, shape: selectedShape };
    }

    if (selectedBehaviors.length > 0) {
      const behaviorsParam = selectedBehaviors;
      body = { ...body, behaviors: behaviorsParam };
    }

    if (selectedColors.length > 0) {
      const colorsParam = selectedColors;
      body = { ...body, colors: colorsParam };
    }
    if (selectedSize) {
      body = { ...body, size: selectedSize };
    }
    axios
      .post("http://localhost:8000/creatures/fish/", body)
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <form onSubmit={handleSubmit} className="fish-filter-form">
      <h3 className="mb-3 text-center">Thai Fish ID</h3>
      <div className="form-group">
        <label>Select Shape:</label>
        <Select
          options={SHAPE_OPTIONS}
          value={selectedShape}
          onChange={(option) => setSelectedShape(option.value)}
        />
      </div>
      <div className="form-group">
        <label>Select Colors:</label>
        <Select isMulti options={COLOR_OPTIONS} onChange={handleColorChange} />
        {selectedColors.length > 0 && (
          <div>
            Selected colors:{" "}
            {selectedColors.map((color) => (
              <span
                key={color}
                className="mx-2"
                style={{
                  backgroundColor: color,
                  color: "white",
                  padding: "0.25rem",
                }}
              >
                {COLOR_OPTIONS.find((option) => option.value === color)?.label}
              </span>
            ))}
          </div>
        )}
      </div>
      <div className="form-group">
        <label>Select Size:</label>
        <select
          className="form-control"
          value={selectedSize}
          onChange={handleSizeChange}
        >
          <option value="">-- Select size --</option>
          <option value="small">Small</option>
          <option value="medium">Medium</option>
          <option value="large">Large</option>
        </select>
      </div>
      <div className="form-group">
        <label>Select Behaviors:</label>
        <Select
          isMulti
          options={BEHAVIOR_OPTIONS}
          onChange={handleBehaviorChange}
        />
        {selectedBehaviors.length > 0 && (
          <div>
            Selected behaviors:{" "}
            {selectedBehaviors.map((behavior) => (
              <span
                key={behavior}
                className="mx-2"
                style={{
                  padding: "0.25rem",
                }}
              >
                {
                  BEHAVIOR_OPTIONS.find((option) => option.value === behavior)
                    ?.label
                }
              </span>
            ))}
          </div>
        )}
      </div>

      <button type="submit" className="btn btn-primary btn-block">
        Filter Fish
      </button>
    </form>
  );
};

export default FishFilter;
