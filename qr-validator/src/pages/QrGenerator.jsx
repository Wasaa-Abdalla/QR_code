import QRCode from "react-qr-code";

function QrGenerator() {
  const url =
    "https://stirring-scone-88d88b.netlify.app//validate/8DEB11A545EE76E";

  return (
    <div className="flex justify-center items-center min-h-screen">
      <QRCode value={url} size={250} />
    </div>
  );
}

export default QrGenerator;