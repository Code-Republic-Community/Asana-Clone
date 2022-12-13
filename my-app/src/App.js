import React, { useState } from "react";
import logo from './logo.svg';
import './App.css';
import { Login } from "./Login";
import { Register } from "./Register";
import { ForgotPassword } from "./ForgotPassword";

function App() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div className="App">  
    {currentForm === "login" && (
      <Login onFormSwitch={toggleForm}/>  )}
    {currentForm === "register" && (
      <Register onFormSwitch={toggleForm}/>  )}
    {currentForm === "forgotpassword" && (
      <ForgotPassword onFormSwitch={toggleForm}/>  )}
  </div>
  );
}

export default App;