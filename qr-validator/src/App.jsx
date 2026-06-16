import { BrowserRouter, Routes, Route } from "react-router-dom";
import ValidationPage from "./pages/ValidationPage";
import QrGenerator from "./pages/QrGenerator";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/validate/8DEB11A545EE76E"
          element={<ValidationPage />}
        />
        <Route path="/" element={<QrGenerator />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;