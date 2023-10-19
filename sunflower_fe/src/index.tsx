import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import router from "./routes/Router";
import {RouterProvider} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.css';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);
