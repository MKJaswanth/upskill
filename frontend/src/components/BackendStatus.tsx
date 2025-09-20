'use client';

import { useState, useEffect } from 'react';

interface BackendStatusProps {
  className?: string;
}

export default function BackendStatus({ className = '' }: BackendStatusProps) {
  const [status, setStatus] = useState<'checking' | 'online' | 'offline'>('checking');
  const [lastChecked, setLastChecked] = useState<Date | null>(null);

  const checkBackendStatus = async () => {
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://pathway-ai-backend.onrender.com';
      const response = await fetch(`${apiUrl}/health`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        setStatus('online');
      } else {
        setStatus('offline');
      }
    } catch {
      setStatus('offline');
    }
    
    setLastChecked(new Date());
  };

  useEffect(() => {
    checkBackendStatus();
    // Check every 30 seconds
    const interval = setInterval(checkBackendStatus, 30000);
    return () => clearInterval(interval);
  }, []);

  const getStatusColor = () => {
    switch (status) {
      case 'online':
        return 'text-green-600 bg-green-100';
      case 'offline':
        return 'text-red-600 bg-red-100';
      case 'checking':
        return 'text-yellow-600 bg-yellow-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  const getStatusText = () => {
    switch (status) {
      case 'online':
        return 'Backend Online';
      case 'offline':
        return 'Backend Offline';
      case 'checking':
        return 'Checking...';
      default:
        return 'Unknown';
    }
  };

  const getStatusIcon = () => {
    switch (status) {
      case 'online':
        return '🟢';
      case 'offline':
        return '🔴';
      case 'checking':
        return '🟡';
      default:
        return '⚪';
    }
  };

  return (
    <div className={`flex items-center space-x-2 ${className}`}>
      <div className={`flex items-center space-x-2 px-3 py-1 rounded-full text-sm font-medium ${getStatusColor()}`}>
        <span>{getStatusIcon()}</span>
        <span>{getStatusText()}</span>
      </div>
      {lastChecked && (
        <button
          onClick={checkBackendStatus}
          className="text-xs text-gray-500 hover:text-gray-700 underline"
          title="Click to check again"
        >
          Check Again
        </button>
      )}
    </div>
  );
}
