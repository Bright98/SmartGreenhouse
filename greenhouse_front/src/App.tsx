import React from "react";
import { BrowserRouter, Switch, Route, Link } from "react-router-dom";
import { Home } from "./pages/index";
import "./App.scss";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
