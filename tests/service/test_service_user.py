from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        name_add = "Leonardo"
        job_add = "TechLead"
        result_expect = "Usuario adicionado com sucesso"
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert result_expect == result

    def test_validate_null_job(self):
        name_null = "Matheus"
        job_null = None
        result_expect = "Usuario nao adicionado"
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert result_expect == result

    def test_validate_null_name(self):
        name_null = None
        job_null = "Dev"
        result_expect = "Usuario nao adicionado"
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert result_expect == result

    def test_add_user_with_name_numeric_expect_error(self):
        name_numeric = 123
        job = "Dev"
        result_expect = "Nome ou Profissão precisa ser um texto"
        service = ServiceUser()

        result = service.add_user(name=name_numeric, job=job)

        assert result_expect == result

    def test_add_user_with_job_numeric_expect_error(self):
        name_numeric = "An Valid Name"
        job = 123
        result_expect = "Nome ou Profissão precisa ser um texto"
        service = ServiceUser()

        result = service.add_user(name=name_numeric, job=job)

        assert result_expect == result

    def test_add_user_already_exists(self):
        name = "Leonardo"
        job = "TechLead"
        result_expect = "Usuario ja cadastrado"
        service = ServiceUser()

        service.add_user(name=name, job=job)
        result = service.add_user(name=name, job=job)

        assert result_expect == result
