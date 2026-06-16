import { BrowserRouter, Routes, Route } from "react-router-dom";
import ValidationPage from "./pages/ValidationPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/validate/:code"
          element={<ValidationPage />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;