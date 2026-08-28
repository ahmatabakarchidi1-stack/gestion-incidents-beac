import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [incidents, setIncidents] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/incidents/')
      .then(response => {
        setIncidents(response.data)
      })
      .catch(error => {
        console.error('Erreur lors du chargement des incidents:', error)
      })
  }, [])

  return (
    <div className="container">
      <h1>Gestion des Incidents Informatiques — BEAC</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Titre</th>
            <th>Statut</th>
            <th>Gravité</th>
          </tr>
        </thead>
        <tbody>
          {incidents.map(incident => (
            <tr key={incident.id}>
              <td>{incident.id}</td>
              <td>{incident.titre}</td>
              <td>
                <span className={`statut statut-${incident.statut}`}>
                  {incident.statut}
                </span>
              </td>
              <td>
                <span className={`gravite gravite-${incident.gravite}`}>
                  {incident.gravite}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App