import React, { useState } from "react";

export const ForgotPassword = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return (
        <div className="auth-form-container">
            <h2>Forgot Password?</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="email">Email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
                <label htmlFor="phone">Phone Number</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="phone" placeholder="+374 ** ** **" id="phone" name="phone" />
                
                <br/>
                <br/>
                <button type="submit">Send Instructions</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('login')}>Log in</button>
        </div>
    )
}