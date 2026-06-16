import QRCode from "react-qr-code";

function QrGenerator() {
  const url =
    "https://your-site.netlify.app/validate/8DEB11A545EE76E";

  return (
    <div className="flex justify-center items-center min-h-screen">
      <QRCode value={url} size={250} />
    </div>
  );
}

export default QrGenerator;