import './App.css';
import React, { useState } from "react";
import FileUploader from './FileUploader';
import axios from 'axios';
const App = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isHidden , setIsHidden] = useState(true);
  const submitForm = () => {
    const formData = new FormData();
    // formData.append("name", name);
    formData.append("file", selectedFile);
    alert("working")
    // alert(selectedFile)
    const UPLOAD_URL="http://127.0.0.1:8000/fileUpload"
    axios
      .post(UPLOAD_URL, formData)
      .then((res) => {
        alert("File Upload success");
      })
      .catch((err) => alert("File Upload Error"));
  };
  const onFileSelectSuccess =(file) =>{
    setIsHidden(false)
    setSelectedFile(file)
  }
  const onFileSelectError = ({ error }) => {
    alert(error)
  }
  return (
    <div className="App">
      <form>
        <h1>Files Upload Hereß</h1>
        <FileUploader onFileSelectSuccess={onFileSelectSuccess} onFileSelectError={onFileSelectError} />

        <button onClick={submitForm} disabled={isHidden}>Submit</button>
      </form>
    </div>
  );
};

export default App;
