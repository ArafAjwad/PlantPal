import './App.css';
import React, { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/air_quality").then(
      res => res.json()
    ).then(
      data => { 
        setData(data);
        setLoading(false);
        console.log(data);
      }
    ).catch(
      error => {
        console.error("Error fetching air quality data:", error);
        setLoading(false);
      }
    )
  }, [])

  return (
    <div className="App">
      {loading ? (
        <p>Loading ...</p>
      ) : (
        <div>
          <h1>Air Quality in {data.city}</h1>
          <p>AQI: {data.aqi}</p>
          <p>Dominant Pollutant: {data.dominant_pollutant}</p>
          <h2>Current Conditions:</h2>
          <p>Humidity: {data.humidity} %</p>
          <p>Pressure: {data.pressure} hPa</p>
          <h2>Forecast:</h2>
          {data.forecast.pm25.map((day, i) => (
            <div key={i}>
              <p>Date: {day.day}</p>
              <p>PM2.5 Average: {day.avg}</p>
              <p>PM2.5 Max: {day.max}</p>
              <p>PM2.5 Min: {day.min}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
