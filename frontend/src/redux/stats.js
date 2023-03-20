import axios from 'axios';
import {
    STATS_LIST,
    BASE_API
} from '../config/index';

const initialState = {
    stats: {
        
        status: 0,
        data: null,
        error: null
    }
}


export const GET_STATS_ACTION  = 'GET_STATS';

export const statsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_STATS_ACTION:
            return {
                ...state,
                stats: action.payload
            }
        default:
            return state;
    }
}


export const getStats = (token) => async(dispatch) => {
    try{
        const res = await axios.get(`${BASE_API+STATS_LIST}`, {
            headers:{
                'Authorization': `Token ${token}`
            }
        });

        dispatch({
            type: GET_STATS_ACTION,
            payload: {
                status: res.status,
                data: res.data,
                error: null
            }
        });
    }catch(error){
        let e = error?.response?.data?.detail||error?.response?.data||error?.message||error;
        dispatch({
            type: GET_STATS_ACTION,
            payload: {
                status: error?.response?.status||500,
                data: null,
                error: e
            }
        });
    }
}

