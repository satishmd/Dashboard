import {Link} from 'react-router-dom'

import './index.css'

const TeamCard = (props)=>{
    const {teamDetails,getFavId} = props
    const {name,img,id} = teamDetails
    const favouriteImg = 'https://assets.ccbp.in/frontend/react-js/star-filled-img.png'


    const onClickFavourite = ()=>{
        getFavId(id)

    }

    return(
        <div className="card-container">
            <Link className="nav-link" to={`/matches/${id}`}>
            <img src={img} alt={name} className="team-logo"/>
            <p>{name}</p>
            </Link>
            <div>
                <img src={favouriteImg} alt='favourite-img' onClick={onClickFavourite} className="star"/>
            </div>
        </div>
    )
}

export default TeamCard