import React, { useState, useEffect } from 'react';

const ServerStatus: React.FC = () => {
  const [serverStatus, setServerStatus] = useState<string>('');
  const [lastUpdatedTime, setLastUpdatedTime] = useState<string>('');

  useEffect(() => {
    fetch('/server_status', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        response.json().then((data) => {
          setServerStatus(
            data.status === 400 ? 'Server is running' : 'Server is not running'
          );
          setLastUpdatedTime(data.current_time);
        });
      })
      .catch((error) => {
        setServerStatus('Server is not running');
      });
  }, []);

  setTimeout(() => {
      fetch('/server_status', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => {
          response.json().then((data) => {
            setServerStatus(
              data.status === 400
                ? 'Server is running'
                : 'Server is not running'
            );
            setLastUpdatedTime(data.current_time);
          });
        })
        .catch((error) => {
          setServerStatus('Server is not running');
        });
  }, 10000);

  return (
    <div>
      <p>
        Server Status: {serverStatus} (Last Updated: {lastUpdatedTime})
      </p>
    </div>
  );
};

export default ServerStatus;
