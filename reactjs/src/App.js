import logo from "./logo.svg";
import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [counter, setCounter] = useState(0);
  useEffect(() => {
    console.log("changed!");
  });
  function clickHandler() {
    setCounter(counter + 1);
  }
  return (
    <div className="App">
      <header className="App-header">
        <button onClick={clickHandler}>Click me!</button>
        <span>Times clicked:</span>
        <span>{counter}</span>
      </header>
    </div>
  );
}

export default App;
