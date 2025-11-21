import React from 'react';

import { useState,useCallback } from 'react';
import { useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';  
import { Box, Typography } from '@mui/material';
const api_endpoint = "http://localhost:9000/locations/v1.0/";
const LocationsList = () => {
  const [locations, setLocations] = useState([]);
  const [loading, setLoading] = React.useState(true);
  const [selectedLocation, setSelectedLocation] = React.useState(null);
  const token = localStorage.getItem('token');  
  console.log('Token in LocationsList:', token);
  useEffect(() => {
    // Fetch locations from an API or data source
  const fetchLocations =async () => {
    try {
      const response = await fetch(api_endpoint, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        }
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setLocations(data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching locations:', error);
    }
  };

  fetchLocations();
 }, []);
     
const handleRowClick = useCallback((location) => {
    console.log('Row clicked:', location);
    setSelectedLocation(location);
    // You can perform any action here, like navigating to a user details page

  }, []);

  return (
    <div>
       {loading ? (
      <div>Loading...</div>
    ) : (
    //   <ul>
    //     {users.map(user => (
    //       <li key={user.id}>
    //         {user.name} - {user.email}
    //       </li>
    //     ))}
    //   </ul>
    <TableContainer component={Paper}>
      <Table width={1000} sx={{ minWidth: 1000}} aria-label="simple table">
        <TableHead>
          <TableRow>
           
            <TableCell align="right">Location Code</TableCell>
            <TableCell align="right">Name</TableCell>
            <TableCell align="right">Latitude</TableCell>
            <TableCell align="right">Longitude</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {locations.map((location) => (
            <TableRow
              key={location.code}
              hover
              style={{ cursor: 'pointer' }}
              onClick={() => handleRowClick(location)}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
            
              <TableCell align="right">{location.code}</TableCell>
              <TableCell align="right">{location.name}</TableCell>
              <TableCell align="right">{location.latitude}</TableCell>
              <TableCell align="right">{location.longitude}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer> 



    )}
    {
        selectedLocation && (
            <Box>
            <h3>Selected Location Details:</h3>
            <Typography variant="body1">
              <strong>Name:</strong> {selectedLocation.name} <br />
             
            </Typography>
            <Typography variant="body1">
              <strong>Latitude:</strong> {selectedLocation.latitude} <br />
            </Typography>
            <Typography variant="body1">
              <strong>Longitude:</strong> {selectedLocation.longitude} <br />
            </Typography>
            </Box>
        )   
     }
    </div>
  );  

}



export default LocationsList;
