import React from "react";
const FileUploader = (props) => {
    // const fileInput = useRef(null)
  
    const handleFileInput = (e) => {
      // handle validations
      const files = e.target.files[0];
      // alert(files.length)
      if (files.length>7){
        props.onFileSelectError({ error: "support 7 no. of file in one time " });
      }
      props.onFileSelectSuccess(files);
    };
  
    return (
        <div className="file-uploader">
            <input type="file" onChange={handleFileInput} multiple/><br></br>
            {/* <button onClick={e => fileInput.current && fileInput.current.click()}/> */}
        </div>
    )
  }
  export default FileUploader;