import React from 'react';

import  './Login.css';
import { Button , TextField} from '@mui/material';

const Login = () => {

  return (
    <form>
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
      <Button type="submit" variant="contained" color="primary" />
     </fieldset>
    </form>
  )
}


export default Login;
