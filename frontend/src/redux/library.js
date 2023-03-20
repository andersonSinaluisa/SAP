import axios from 'axios';
import { BASE_API, LIBRARY_CREATE, LIBRARY_LIST, LIBRARY_COMPARE } from 'src/config';




const initialState = {
    createLibrary: {
        data: null,
        status: 0,
        error: null
    },
    libraryList: {
        data: [],
        status: 0,
        error: null
    },
    compareLibrary: {
        data: null,
        status: 0,
        error: null
    }
}
export const GET_LIBRARY_LIST = 'GET_LIBRARY_LIST';
export const CREATE_LIBRARY = 'CREATE_LIBRARY';
export const COMPARE_LIBRARY = 'COMPARE_LIBRARY';

export const libraryReducer = (state = initialState, action) => {
    switch (action.type) {
        case CREATE_LIBRARY:
            return {
                ...state,
                createLibrary: action.payload
            }
        case GET_LIBRARY_LIST:
            return {
                ...state,
                libraryList: action.payload
            }
        case COMPARE_LIBRARY:
            return {
                ...state,
                compareLibrary: action.payload
            }
        default:
            return state;
    }
}

export const createLibrary = (title, author, description, file, token) => async (dispatch) => {

    //get token from store redux


    try {
        let formdata = new FormData();
        formdata.append('title', title);
        formdata.append('author', author);
        formdata.append('description', description);
        formdata.append('file', file);
        const res = await axios.post(BASE_API + LIBRARY_CREATE, formdata, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'Authorization': 'Token ' + token
            }
        });

        dispatch({
            type: CREATE_LIBRARY,
            payload: {
                data: res.data,
                status: res.status,
                error: null
            }
        })
    } catch (error) {
        let e = error?.response?.data?.detail || error?.message || "Something went wrong";
        dispatch({
            type: CREATE_LIBRARY,
            payload: {
                data: null,
                status: error?.response?.status || 400,
                error: e
            }
        })
    }

}


export const getLibraryList = (perPage = 15, page = 1, token) => async (dispatch) => {
    try {
        const res = await axios.get(BASE_API + LIBRARY_LIST, {
            params: {
                perPage: perPage,
                page: page
            },
            headers: {
                Authorization: 'Token ' + token
            }
        });

        dispatch({
            type: GET_LIBRARY_LIST,
            payload: {
                data: res.data,
                status: res.status,
                error: null
            }
        })
    } catch (error) {
        let e = error?.response?.data?.detail || error?.message || "Something went wrong";
        dispatch({
            type: GET_LIBRARY_LIST,
            payload: {
                data: [],
                status: error?.response?.status || 400,
                error: e
            }
        })
    }
}


export const compareLibrary = (file1, file2, token) => async (dispatch) => {
    try {
        let formdata = new FormData();
        formdata.append('file1', file1);
        formdata.append('file2', file2);
        const res = await axios.post(BASE_API + LIBRARY_COMPARE, formdata, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'Authorization': 'Token ' + token
            }
        });

        dispatch({
            type: COMPARE_LIBRARY,
            payload: {
                data: res.data,
                status: res.status,
                error: null
            }
        })
    } catch (error) {
        let e = error?.response?.data?.detail || error?.message || "Something went wrong";
        dispatch({
            type: COMPARE_LIBRARY,
            payload: {
                data: null,
                status: error?.response?.status || 400,
                error: e
            }
        })

    }
}
