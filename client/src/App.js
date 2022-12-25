import React, { useState } from 'react';
import { GooglePicker } from 'react-color';
import Slider from '@material-ui/core/Slider';
import axios from "axios";


const App = () => {
  const [numColorPickers, setNumColorPickers] = useState(0);
  const [colors, setColors] = useState([]);

  const handleSliderChange = (event, value) => {
    setNumColorPickers(value);
    setColors(colors.slice(0, numColorPickers));
  };

  const sendColors = () => {
    console.log(`sending colors: ${colors}`)
    axios.post("http://localhost:8000", colors).then(response => {
      // The server returned a successful status code
      console.log(response.data);
    });
  };

  const handleColorChange = (index, color) => {
    const newColors = [...colors];
    newColors[index] = color.rgb;
    setColors(newColors.slice(0, numColorPickers));
	};

  return (
    <div>
      <header>
        <h1>My App</h1>
      </header>
      <main>
        <h2>Color Picker List</h2>
        <div className="row">
          {[...Array(numColorPickers)].map((_, index) => (
            <div key={index} className="col s3">
              <GooglePicker
                color={colors[index]}
                onChange={(color) => handleColorChange(index, color)}
              />
            </div>
          ))}
        </div>
        <Slider
          value={numColorPickers}
          min={1}
          max={5}
          onChange={handleSliderChange}
        />
        <button id="my-button" className="button" onClick={sendColors}>Send Colors</button>
      </main>
      <footer>
        <p>Copyright 2021</p>
      </footer>
	</div>
  )

		  }


export default App;