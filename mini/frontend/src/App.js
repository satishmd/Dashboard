import { BrowserRouter, Route, Switch } from "react-router-dom" 
import './App.css'
import Home from "./Components/Home"
import TeamMatches from "./Components/TeamMatches"


const App = () => (
    <BrowserRouter>
        <Switch>
            <Route exact path="/" component={Home}/>
            <Route exact path="/matches/:id" component={TeamMatches}/>
        </Switch>
    </BrowserRouter>
)

export default App