import React,{useEffect} from "react";
import { useSelector ,useDispatch} from "react-redux";
import { useNavigate } from "react-router-dom";
import { login, logout } from "../redux/auth";



const AuthContext = React.createContext({
    token: null,
    user_id: null,
    email: null,
    fecha: null,
    permissions: [],
    is_superuser: null,
    first_name: null,
    last_name: null,
    is_staff: null,
    is_active: null,
    date_joined: null,
});

export const AuthProvider = ({ children }) => {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const [token, setToken] = React.useState("");
    const _token = useSelector((state) => state.auth.token);

    useEffect(() => {
        setToken(_token.token);

       if (_token.token!==""){
        navigate("/app/app");
       }
     
    }, [_token])
    

    const handleLogin = (username, password) => {
        dispatch(login({
             username, password,
        }));

        navigate("/app/app");

    };

    const handleLogout = () => {
        dispatch(logout(token.token))
        setToken(null);
    };

    const value = {
        ..._token,
        onLogin: handleLogin,
        onLogout: handleLogout,
    };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return React.useContext(AuthContext);
};