import React, { useEffect, useState } from "react";
import { customFetch } from "../utils/Index";
import "../App.css";

const Home: React.FC = () => {
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("Summary...");

  const handleSummarize = () => {
    // Replace with real logic if desired
    setSummary(`Here is a summary for the video at: \n${url}`);
  };
  const getSummary = async () => {
    try {
      // Adjust the expected response type if your API returns data differently.
      const response = await customFetch.post("/", {
        url: url,
      });
      console.log(response.data);
      //   setSummary(response.data);
    } catch (err) {
      console.error("Error fetching products:", err);
    }
  };
  const handleCurrentIndustry = () => {
    // Replace with real logic if needed
    alert("Current Industry functionality here.");
  };

  return (
    <div className="summarizer-container">
      {/* Title */}
      <h1 className="title">Youtube Summarizer</h1>

      {/* Instructions in a centered box */}
      <div className="instructions-box">
        <p>
          Enter your Youtube url below to get a summary! <br />
          You can choose the industry and type of content to get a better
          summary.
        </p>
      </div>

      {/* Search bar + icon */}
      <div className="search-bar">
        <input
          className="url-input"
          type="text"
          placeholder="Enter Youtube URL!"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <span className="search-icon">&#128269;</span>
      </div>

      {/* Buttons underneath */}
      <div className="button-row">
        <button className="summarize-button" onClick={getSummary}>
          Summarize
        </button>
        <button className="industry-button" onClick={handleCurrentIndustry}>
          "Current Industry"
        </button>
      </div>

      {/* Summary box */}
      <div className="summary-box">{summary}</div>
    </div>
  );
};

export default Home;
