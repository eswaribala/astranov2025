import React from 'react';
import { useFormik } from 'formik';
import  './Login.css';
import { Button , TextField} from '@mui/material';
import * as Yup from 'yup';

const valiationSchema = Yup.object({
  userName: Yup.string().required('User Name is required'),
  password: Yup.string().required('Password is required')
});



const Login = () => {


  const formik = useFormik({
    initialValues: {
      userName: '',
      password: ''
    },
    validationSchema: valiationSchema,
    onSubmit: (values) => {
      console.log('Form data', values);
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
