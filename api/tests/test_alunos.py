import pytest
from api.models import Aluno
from django.urls import reverse
from datetime import date

@pytest.mark.django_db
class TestAlunoCRUD:
    @pytest.fixture
    def aluno_data(self):
        return {
            'name': 'João Ferreira',
            'description': 'Estudante de Direito',
            'birthday': date(2000, 12, 12),
            'email': 'joaoferr@test.com',
            'phone': '0123456789',
            'registration_number': '123456',
        }

    def test_create_aluno(self, aluno_data, client):
        url = reverse('aluno-list')
        response = client.post(url, data=aluno_data)
        
        assert response.status_code == 201
        assert Aluno.objects.count() == 1
        assert Aluno.objects.first().name == aluno_data['name']

    def test_read_aluno(self, aluno_data, client):
        aluno = Aluno.objects.create(**aluno_data)
        url = reverse('aluno-detail', args=[aluno.id])
        response = client.get(url)
        
        assert response.status_code == 200
        assert aluno.name in response.content.decode()
        assert aluno.description in response.content.decode()

    def test_update_aluno(self, aluno_data, client):
        aluno = Aluno.objects.create(**aluno_data)
        update_data = {
             'name': 'João Ferreira Atualiziado',
            'description': 'Estudante de Direito Atualziado',
            'birthday': date(2000, 1, 1),
            'email': 'joaoferr2@test.com',
            'phone': '01234567892',
            'registration_number': '1234562',
        }
        url = reverse('aluno-detail', args=[aluno.id])
        response = client.put(url, data=update_data, content_type='application/json')

        print(response.content)
        
        assert response.status_code == 200
        aluno.refresh_from_db()
        assert aluno.name == update_data['name']

    def test_delete_aluno(self, aluno_data, client):
        aluno = Aluno.objects.create(**aluno_data)
        url = reverse('aluno-detail', args=[aluno.id])
        response = client.delete(url)
        
        assert response.status_code == 204
        assert Aluno.objects.count() == 0
