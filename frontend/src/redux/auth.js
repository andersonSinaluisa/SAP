import axios from "axios";
import {
  BASE_API,
  LOGIN_PATH,
  USER_LIST,
  USER_CREATE,
  USER_UPDATE,
  USER_DELETE,
  USER_LOGOUT,
} from "../config/index";

/**
 * @const
 * @type JSONObject
 * @default
 */
const init = {
  token: {
    token: "",
    user_id: "",
    email: "",
    fecha: "",
    permissions: [],
    is_superuser: false,
      first_name: "",
      last_name: "",
      is_staff: false,
      is_active: false,
      date_joined: "",
  },
  user: null,
  isLogin: false,
  reset_confirm: 0,
  reset_request: 0,
  error: {
    message: "",
    status: 0,
  },
  get_users: {
    message: "",
    status: 0,
    data: [],
  },
  create_user: {
    message: "",
    status: 0,
  },
  update_user: {
    message: "",
    status: 0,
  },
  delete_user: {
    message: "",
    status: 0,
  },
};

/** @constant
    @type {string}
    @default
*/
const LOGIN = "LOGIN";

/** @constant
 * @type {string}
 * @default
 *
 */
const LOGOUT = "LOGOUT";

/** @constant
 * @type {string}
 * @default
 *
 */
const ERROR_LOGIN = "ERROR_LOGIN";

/** @constant
 * @type {string}
 * @default
 *
 */
export const CREATE_USER = "CREATE_USER";
/** @constant
 * @type {string}
 * @default
 *
 */
const GET_USERS = "GET_USERS";

export const UPDATE_USER = "UPDATE_USER";

export const DELETE_USER = "DELETE_USER";

/**
 * @sumary funcion reducer para el modulo de autenticación
 * @param {JsonObject} state
 * @param {JsonObject} action
 * @returns {JsonObject}
 */

export const authReducer = (state = init, action) => {
  switch (action.type) {
    case LOGIN:
      return {
        ...state,
        token: action.payload.token,
        user: action.payload.user,
        isLogin: true,
      };
    case LOGOUT:
      return init;
    case ERROR_LOGIN:
      return {
        ...state,
        error: action.payload,
      };
    case GET_USERS:
      return {
        ...state,
        get_users: action.payload,
      };
    case CREATE_USER:
      return {
        ...state,
        create_user: action.payload,
      };
    case UPDATE_USER:
      return {
        ...state,
        update_user: action.payload,
      };
    case DELETE_USER:
      return {
        ...state,
        delete_user: action.payload,
      };

    default:
      return state;
  }
};

/**
 * @sumary funcion para iniciar sesion
 * @param {String} user
 * @param {String} password
 * @returns {JsonObject}
 *
 */
export const login = (data) => async (dispatch) => {
  try {
    console.log(BASE_API + LOGIN_PATH);
    const res = await axios.post(BASE_API + LOGIN_PATH, data);

    dispatch({
      type: LOGIN,
      payload: { token: res.data, user: data.username, isLogin: true },
    });
  } catch (error) {
    console.log(error);
    if (error.response) {
      if (error.response.status === 400) {
        dispatch({
          type: ERROR_LOGIN,
          payload: { status: 400, msj: "Usuario o contraseña incorrectos" },
        });
      }
    } else {
      dispatch({
        type: ERROR_LOGIN,
        payload: { status: 500, msj: "Ocurrio un error" },
      });
    }
  }
};

/**
 * @sumary funcion para obtener los usuarios
 * @returns {JsonObject}
 *
 */
export const getUsers = (token) => async (dispatch) => {
  try {
    const res = await axios.get(BASE_API + USER_LIST, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    dispatch({ type: GET_USERS, payload: { status: 200, data: res.data } });
  } catch (error) {
    dispatch({
      type: GET_USERS,
      payload: {
        status: error.response?.status || 500
        , msj: "Ocurrio un error",
        data: []
      },
    });


  }
};

/**
 * @sumary funcion para crear un usuario
 * @param {JsonObject} data
 * @returns {JsonObject}
 *
 */
export const createUser = (data, token) => async (dispatch) => {
  try {
    const res = await axios.post(BASE_API + USER_CREATE, data);
    dispatch({
      type: CREATE_USER,
      payload: { status: res.status, message: "Usuario creado con exito" },
    });
  } catch (error) {
    if (error.response) {
      if (error.response.status === 400) {
        dispatch({
          type: CREATE_USER,
          payload: { status: 400, message: "Ocurrio un error" },
        });
      }
    } else {
      dispatch({
        type: CREATE_USER,
        payload: { status: 500, message: "Ocurrio un error" },
      });
    }
  }
};
/**
 * @sumary funcion para actualizar un usuario
 * @param {JsonObject} data
 * @param {int} id
 * @returns {JsonObject}
 *
 */
export const updateUser = (data, id, token) => async (dispatch) => {
  try {
    const res = await axios.post(BASE_API + USER_UPDATE + id, data, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    dispatch({
      type: UPDATE_USER,
      payload: { status: res.status, message: "Usuario actualizado con exito" },
    });
  } catch (error) {
    if (error.response) {
      if (error.response.status === 400) {
        dispatch({
          type: UPDATE_USER,
          payload: { status: 400, message: "Ocurrio un error" },
        });
      }
    } else {
      dispatch({
        type: UPDATE_USER,
        payload: { status: 500, message: "Ocurrio un error" },
      });
    }
  }
};

/**
 * @sumary funcion para eliminar un usuario
 * @param {int} id
 * @returns {JsonObject}
 *
 */
export const deleteUser = (id, token) => async (dispatch) => {
  try {
    const res = await axios.post(
      BASE_API + USER_DELETE + id,
      {},
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
    dispatch({
      type: DELETE_USER,
      payload: { status: res.status, message: "Usuario eliminado con exito" },
    });
  } catch (error) {
    if (error.response) {
      if (error.response.status === 400) {
        dispatch({
          type: DELETE_USER,
          payload: { status: 400, message: "Ocurrio un error" },
        });
      }
    } else {
      dispatch({
        type: DELETE_USER,
        payload: { status: 500, message: "Ocurrio un error" },
      });
    }
  }
};

/**
 * @sumary funcion para limpiar un estado
 * @param {String} type
 * @param {JsonObject} data
 * @returns {JsonObject}
 *
 */
export const clearState = (type, data) => (dispatch) => {
  dispatch({ type, payload: data });
};

/**
 * @sumary funcion para cerrar sesion
 * @param {String} token
 * @returns {JsonObject}
 *
 */
export const logout = (token) => async (dispatch) => {
  try {
    const res = await axios.post(
      BASE_API + USER_LOGOUT,
      {},
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );

    dispatch({
      type: LOGOUT,
      payload: { token: {}, user: null, isLogin: false },
    });
  } catch (error) {
    if (error.response) {
      if (error.response.status === 400) {
        dispatch({
          type: ERROR_LOGIN,
          payload: { status: 400, msj: "Ocurrio un error" },
        });
      }
    } else {
      dispatch({
        type: ERROR_LOGIN,
        payload: { status: 500, msj: "Ocurrio un error" },
      });
    }
  }
};
