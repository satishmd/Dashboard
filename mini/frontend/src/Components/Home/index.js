import {Component} from 'react'

import './index.css'
import TeamCard from '../TeamCard' 
import FavouriteCard from '../FavouriteCard'

class Home extends Component{
    state = {teamsData : [],favId:''}

    componentDidMount() {
        this.getTeams()
      }
    
    getTeams = async () =>{
        const response = await fetch('http://localhost:8000/api/teams')
        const data = await response.json()
        const formattedData = data.map(eachItem => ({
            id: eachItem.id,
            name: eachItem.name,
            img: eachItem.img,
          }))
        
        this.setState({teamsData:formattedData})
    }

    getFavId = value => {
        this.setState({favId:value})
    }

    removeFav = () =>{
        this.setState({favId:''})
    }


    render(){
        const {teamsData,favId} = this.state
        const favTeam = teamsData.find(team=>team.id===favId)
        console.log(favTeam)
        return(
            <div className="main-container">
                <div className="heading-container">
                <img src="https://assets.ccbp.in/frontend/react-js/ipl-logo-img.png" alt="apl logo" className="apl-logo"/>
                <h1 className="main-heading">IPL Dashboard</h1>
                </div>
                <div className="teams-container">
                    {
                       teamsData.map(eachTeam=>(
                           <TeamCard key={eachTeam.id} teamDetails={eachTeam} getFavId={this.getFavId}/>
                       )) 
                    }
                </div>
                {favTeam?<div className="fav-container">
                        <FavouriteCard favTeam={favTeam}/>
                        <div><img src="https://assets.ccbp.in/frontend/react-js/comments-app/delete-img.png" alt="delete" onClick={this.removeFav} className="delete"/></div>
                        </div>:<p className="favourite">click on star to add your favourite team</p>}
            </div>
        )
    }
}

export default Home