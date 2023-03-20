import PropTypes from 'prop-types';
// @mui
import { Box, Card, Link, Typography, Stack } from '@mui/material';
import { styled } from '@mui/material/styles';
// utils
import { fCurrency } from '../../../utils/formatNumber';
// components
import Label from '../../../components/label';
import { ColorPreview } from '../../../components/color-utils';

// ----------------------------------------------------------------------

const StyledProductImg = styled('img')({
  top: 0,
  width: '100%',
  height: '100%',
  objectFit: 'cover',
  position: 'absolute',
});

// ----------------------------------------------------------------------

DocCard.propTypes = {
  doc: PropTypes.object,
};

export default function DocCard({ doc }) {
  const { id_biblioteca, id_usuario, autor, descripcion, documento, fecha_subida,type_doc } = doc;

  return (
    <Card>
      <Box sx={{ pt: '100%', position: 'relative' }}>
     
          <Label
            variant="filled"
            color={'info'}
            sx={{
              zIndex: 9,
              top: 16,
              right: 16,
              position: 'absolute',
              textTransform: 'uppercase',
            }}
          >
            {autor}
          </Label>
      
        <StyledProductImg alt={descripcion} src={ '/assets/icons/'+type_doc+'.png'} />
      </Box>

      <Stack spacing={2} sx={{ p: 3 }}>
        <Link color="inherit" underline="hover">

          
          <Typography variant="subtitle2" noWrap>
            {
              descripcion
            }
          </Typography>
        </Link>

        <Stack direction="row" alignItems="center" justifyContent="space-between">
          <Typography variant="subtitle1">
            <Typography
              component="span"
              variant="body1"
              sx={{
                color: 'text.disabled',
              }}
            >
              {fecha_subida }
            </Typography>
        
          </Typography>
        </Stack>
      </Stack>
    </Card>
  );
}
