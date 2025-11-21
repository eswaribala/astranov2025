import React from 'react';
import { useFormik } from 'formik';
import  './Login.css';
import { Button , TextField} from '@mui/material';
import * as Yup from 'yup';
import { useNavigate } from 'react-router-dom';

const valiationSchema = Yup.object({
  userName: Yup.string().required('User Name is required'),
  password: Yup.string().required('Password is required')
});

const api_endpoint = "http://localhost:9000/login";


const Login = ({loginStatus}) => {

 const navigate = useNavigate();
  const formik = useFormik({
    initialValues: {
      userName: '',
      password: ''
    },
    validationSchema: valiationSchema,
    onSubmit: (values) => {
      
      const jsondata={
        "username": values.userName,
        "password": values.password
      }
      console.log('Form data', jsondata);
     const jsondataString = JSON.stringify(jsondata);
     console.log('Form data', jsondataString);
     fetch(api_endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: jsondataString
     })
     .then(response => {
      if (!response.ok) {
    }
      return response.json();
     })
     .then(data => {
      console.log('Success:', data.access_token);
      localStorage.setItem('token', data.access_token);
      loginStatus(true);
      navigate('/dashboard');
     })
     .catch((error) => {
      console.error('Error:', error);
     });
    }
  });


  return (
    <form onSubmit={formik.handleSubmit}>
      <fieldset>
      <legend>Login</legend>
      <TextField id="userName"
         name="userName"
         label="User Name"
         variant="outlined"
         onChange={formik.handleChange}
         value={formik.values.userName}
         onError={formik.touched.userName && formik.errors.userName && Boolean(formik.errors.userName)}
         helperText={formik.touched.userName &&formik.errors.userName}
         fullWidth
         margin="normal" />
      <TextField 
          label="Password" 
          name="password" 
          type="password" 
          variant='filled'
          onChange={formik.handleChange}
          value={formik.values.password}
         onError={formik.touched.password && formik.errors.password && Boolean(formik.errors.password)}
         helperText={formik.touched.password &&formik.errors.password}
         fullWidth
         margin="normal"  />
      <Button type="submit" variant="contained" color="primary">
        Login
        </Button>
     </fieldset>
    </form>
  )
}


export default Login;
