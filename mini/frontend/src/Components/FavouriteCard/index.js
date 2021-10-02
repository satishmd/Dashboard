
import './index.css'


const FavouriteCard = (props)=>{
    const {favTeam} = props

    return(
        <div className="favourite-nav-link" >
            <img src={favTeam.img} alt={favTeam.name} className="team-logo"/>
        </div>
    )
}

export default FavouriteCard